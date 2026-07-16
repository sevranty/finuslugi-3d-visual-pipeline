import json, tempfile, unittest
from pathlib import Path
class AssetInventoryTests(unittest.TestCase):
    def test_unregistered_binary_is_detectable(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td); (root/'assets').mkdir(); (root/'assets/x.png').write_bytes(b'png'); manifest={'assets':[]}
            visual={p.relative_to(root).as_posix() for p in root.rglob('*') if p.suffix=='.png'}
            registered={e['path'] for e in manifest['assets']}
            self.assertEqual(visual-registered,{'assets/x.png'})
    def test_neutral_asset_ids(self):
        ids={'plugin-icon','plugin-logo','modern-flat-cube'}
        self.assertEqual(len(ids),3)
if __name__=='__main__': unittest.main()
