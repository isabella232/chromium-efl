// Copyright 2014 Samsung Electronics Inc. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#ifndef MEDIA_BASE_TIZEN_WEBAUDIO_MEDIA_CODEC_INFO_TIZEN_H_
#define MEDIA_BASE_TIZEN_WEBAUDIO_MEDIA_CODEC_INFO_TIZEN_H_

namespace media {

// This structure holds the information about the audio file
// determined by MediaCodec that is needed by the audio decoder to
// create the necessary destination bus.
struct WebAudioMediaCodecInfoTizen {
  unsigned long channel_count;
  unsigned long sample_rate;
  unsigned long number_of_frames;
};

}  // namespace media
#endif // MEDIA_BASE_TIZEN_WEBAUDIO_MEDIA_CODEC_INFO_TIZEN_H_