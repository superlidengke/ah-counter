from parser.audioTools import AudioTools
from pathlib import Path

home_dir = Path(__file__).parent.parent


class TestAudioTools:  # must start with Test

    def test_get_info(self):
        audio_info = AudioTools.get_info(Path(home_dir, "test/res/a1.mp3"))
        assert audio_info['duration'] == 13500

    def test_export(self):
        out_file = Path(home_dir, "debug/out/test_export.mp3")
        out_file.parent.mkdir(parents=True, exist_ok=True)
        AudioTools.export(Path(home_dir, "test/res/a1.mp3"), out_file, 1.5, 4)
        assert out_file.exists()
        assert AudioTools.get_info(out_file)['duration'] == 2500
