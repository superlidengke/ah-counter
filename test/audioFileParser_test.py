from parser.audioFileParser import AudioFileParser


class TestAudioFileParser:  # must start with Test

    def test_get_info(self):
        audio_file_parser = AudioFileParser()
        assert "World" is audio_file_parser.get_info()




