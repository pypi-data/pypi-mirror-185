#define _CRT_SECURE_NO_WARNINGS 
#define NOMINMAX
#define _Z_DEBUG
#include "func.hpp"
#include "pybind11/pybind11.h"
#include "pybind11/numpy.h"
#include "audio-capture-helper.hpp"

#pragma comment(lib, "User32.lib")
#pragma comment(lib, "psapi.lib")
#pragma comment(lib, "dwmapi.lib")
#pragma comment(lib, "ksuser.lib")
#pragma comment(lib, "mmdevapi.lib")
#pragma comment(lib, "mfplat.lib")

#include <unordered_map>

std::unordered_map<HWND, AudioCaptureHelper*> hwnd2capture;

int init_audio(long long hwnd_int, std::string format){
  Z_DEBUG("init_audio starts\n");
  HWND hwnd = (HWND) hwnd_int;
  if (hwnd2capture.find(hwnd)!=hwnd2capture.end()) return -1;
  auto pid = process_windows::HWND2pid(hwnd);
  if (format=="WAVE_FORMAT_PCM"){
    hwnd2capture[hwnd] = new AudioCaptureHelper(get_wave_format_pcm(), pid, hwnd);
  }
  else if (format=="WAVE_FORMAT_IEEE_FLOAT"){
    hwnd2capture[hwnd] = new AudioCaptureHelper(get_wave_format_float(), pid, hwnd);
  }
  else{
    Z_ERROR("unknown format: %s\n", format.c_str());
  }
  return 0;
}

int delete_audio(long long hwnd_int){
  Z_DEBUG("delete_audio starts\n");
  HWND hwnd = (HWND) hwnd_int;
  if (hwnd2capture.find(hwnd)==hwnd2capture.end()) return -1;
  delete hwnd2capture[hwnd];
  hwnd2capture.erase(hwnd);
  return 0;
}

template <typename T>
pybind11::array_t<T> get_audio(long long hwnd_int){
  HWND hwnd = (HWND) hwnd_int;
  if (hwnd2capture.find(hwnd)==hwnd2capture.end()) return pybind11::array_t<T>(0);
  auto capture = hwnd2capture[hwnd];
  BYTE* byte_data;
  UINT32 num_frames;
  capture->GetPacket(&byte_data, &num_frames);
  T* data = reinterpret_cast<T*> (byte_data);
  pybind11::buffer_info data_info(
    data, sizeof(T), pybind11::format_descriptor<T>::value, 1, {num_frames*2}, {sizeof(T)}
  );
  auto numpy_data = pybind11::array_t<T>(data_info);
  return numpy_data;
}


namespace py = pybind11;
using namespace pybind11::literals;
PYBIND11_MODULE(wcap_core, m) {
  m.def("init_audio", &init_audio, "Test audio usage");
  m.def("get_audio_pcm", &(get_audio<int16_t>), "Test audio usage");
  m.def("get_audio_ieee_float", &(get_audio<float>), "Test audio usage");
  m.def("delete_audio", &delete_audio, "Test audio usage");
}