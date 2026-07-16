import sys, tempfile, unittest
from pathlib import Path
SCRIPTS=Path(__file__).resolve().parents[1]/"scripts"
sys.path.insert(0,str(SCRIPTS))
import validation_lib as mod
class RelativePathTests(unittest.TestCase):
    def test_nested_valid(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td); (root/"assets").mkdir(); (root/"assets/a.json").write_text("{}")
            d=root/"skills/x/references"; d.mkdir(parents=True); doc=d/"a.md"; doc.write_text("`../../../assets/a.json`")
            self.assertEqual(mod.broken_relative_paths(root,[doc]),[])
    def test_nested_missing(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td); d=root/"skills/x/references"; d.mkdir(parents=True); doc=d/"a.md"; doc.write_text("`../../../assets/missing.json`")
            self.assertTrue(mod.broken_relative_paths(root,[doc]))
    def test_root_relative_rule(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td); (root/"assets").mkdir(); (root/"assets/a.json").write_text("{}")
            doc=root/"a.md"; doc.write_text("[/asset](/assets/a.json)")
            self.assertEqual(mod.broken_relative_paths(root,[doc]),[])
if __name__=="__main__": unittest.main()
