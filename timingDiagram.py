import wavedrom
svg = wavedrom.render("""
{ "signal": [
 { "name": "UART", "wave": "x3.4.5.|6.7.7.8.x", "data": 'length cmd string dummy value(LB) value(HB) checksum',                     "phase": 0.5 },
]}""")
svg.saveas("demo1.svg")
