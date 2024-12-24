#!/bin/bash

for lineno in "$((6-1))"   "6" "$(( 6+1))"; do echo "TCDataProcessing/pipelines/Histogram.py                      |  $(git blame -L6,6 TCDataProcessing/pipelines/Histogram.py)"; done
for lineno in "$((15-1))" "15" "$((15+1))"; do echo "TCDataProcessing/pipelines/Histogram.py                      |  $(git blame -L15,15 TCDataProcessing/pipelines/Histogram.py)"; done
for lineno in "$((6-1))"   "6" "$(( 6+1))"; do echo "TCDataProcessing/pipelines/DensityPlot.py                    |  $(git blame -L6,6 TCDataProcessing/pipelines/DensityPlot.py)"; done
for lineno in "$((15-1))" "15" "$((15+1))"; do echo "TCDataProcessing/pipelines/DensityPlot.py                    |  $(git blame -L15,15 TCDataProcessing/pipelines/DensityPlot.py)"; done
for lineno in "$((6-1))"   "6" "$(( 6+1))"; do echo "TCDataProcessing/pipelines/TrackMap.py                       |  $(git blame -L6,6 TCDataProcessing/pipelines/TrackMap.py)"; done
for lineno in "$((15-1))" "15" "$((15+1))"; do echo "TCDataProcessing/pipelines/TrackMap.py                       |  $(git blame -L15,15 TCDataProcessing/pipelines/TrackMap.py)"; done
for lineno in "$((6-1))"   "6" "$(( 6+1))"; do echo "TCDataProcessing/pipelines/StormCenteredTrack.py             |  $(git blame -L6,6 TCDataProcessing/pipelines/StormCenteredTrack.py)"; done
for lineno in "$((9-1))"   "9" "$(( 9+1))"; do echo "TCDataProcessing/pipelines/StormCenteredTrack.py             |  $(git blame -L9,9 TCDataProcessing/pipelines/StormCenteredTrack.py)"; done
for lineno in "$((15-1))" "15" "$((15+1))"; do echo "TCDataProcessing/scripts/python/reduce_trackfile.py          |  $(git blame -L15,15 TCDataProcessing/scripts/python/reduce_trackfile.py)"; done
for lineno in "$((50-1))" "50" "$((50+1))"; do echo "TCDataProcessing/scripts/python/reduce_trackfile.py          |  $(git blame -L50,50 TCDataProcessing/scripts/python/reduce_trackfile.py)"; done
for lineno in "$((42-1))" "42" "$((42+1))"; do echo "TCDataProcessing/scripts/python/tests/test_record_tracks.py  |  $(git blame -L42,42 TCDataProcessing/scripts/python/tests/test_record_tracks.py)"; done
for lineno in "$((43-1))" "43" "$((43+1))"; do echo "TCDataProcessing/scripts/python/tests/test_record_tracks.py  |  $(git blame -L43,43 TCDataProcessing/scripts/python/tests/test_record_tracks.py)"; done
for lineno in "$((45-1))" "45" "$((45+1))"; do echo "TCDataProcessing/scripts/python/tests/test_record_tracks.py  |  $(git blame -L45,45 TCDataProcessing/scripts/python/tests/test_record_tracks.py)"; done
for lineno in "$((47-1))" "47" "$((47+1))"; do echo "TCDataProcessing/scripts/python/tests/test_record_tracks.py  |  $(git blame -L47,47 TCDataProcessing/scripts/python/tests/test_record_tracks.py)"; done
for lineno in "$((51-1))" "51" "$((51+1))"; do echo "TCDataProcessing/scripts/python/tests/test_record_tracks.py  |  $(git blame -L51,51 TCDataProcessing/scripts/python/tests/test_record_tracks.py)"; done
for lineno in "$((42-1))" "42" "$((42+1))"; do echo "TCDataProcessing/scripts/matlab/tests/test_track_map.py      |  $(git blame -L42,42 TCDataProcessing/scripts/matlab/tests/test_track_map.py)"; done
for lineno in "$((43-1))" "43" "$((43+1))"; do echo "TCDataProcessing/scripts/matlab/tests/test_track_map.py      |  $(git blame -L43,43 TCDataProcessing/scripts/matlab/tests/test_track_map.py)"; done
for lineno in "$((45-1))" "45" "$((45+1))"; do echo "TCDataProcessing/scripts/matlab/tests/test_track_map.py      |  $(git blame -L45,45 TCDataProcessing/scripts/matlab/tests/test_track_map.py)"; done
for lineno in "$((47-1))" "47" "$((47+1))"; do echo "TCDataProcessing/scripts/matlab/tests/test_track_map.py      |  $(git blame -L47,47 TCDataProcessing/scripts/matlab/tests/test_track_map.py)"; done
for lineno in "$((51-1))" "51" "$((51+1))"; do echo "TCDataProcessing/scripts/matlab/tests/test_track_map.py      |  $(git blame -L51,51 TCDataProcessing/scripts/matlab/tests/test_track_map.py)"; done

