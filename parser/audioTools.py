from pydub import AudioSegment


class AudioTools:

    @staticmethod
    def export(audio_file, out_file, start_time, end_time):
        sound_data = AudioSegment.from_mp3(audio_file)
        out_part = sound_data[start_time*1000:end_time*1000]
        out_part.export(out_file, format="mp3")

    @staticmethod
    def get_info(audio_file):
        sound_data = AudioSegment.from_mp3(audio_file)
        duration = len(sound_data)
        return {"duration": duration}

