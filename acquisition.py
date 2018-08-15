import datajoint as dj

import subject
import reference

schema = dj.schema(dj.config['names.{}'.format(__name__)])

'''
To simplify from Alyx schema, dropping file repositories as core
parts of tables and moving to per-table blobs. A facility for
tracking data provenance could still made avaialble via a table
linked into individual model records as a non-primary attribute.

This is probably not ideal w/r/t Alyx -

one idea would be to merge use external storage with example
field def being:

  aligned_movie :  external  # motion-aligned movie

and also have a separate 'phase 1' data schema, which is then coupled
with phase 2+ for higher level data products.

Also note: TimeScale items missing wrt TimeSeries items, which were:

- PupilTracking.xyd
- PupilTracking.movie
- HeadTracking.xy_theta
- HeadTracking.movie

TimeScale not yet defined

# SKIPPED:
# <class 'data.models.DataRepositoryType'>
# <class 'data.models.DataRepository'>
# <class 'data.models.DatasetType'>
# <class 'data.models.Dataset'>
# <class 'data.models.FileRecord'>
# <class 'data.models.DataCollection'>
# <class 'data.models.Timescale'>
# <class 'data.models.TimeSeries'>
# <class 'data.models.EventSeries'>
# <class 'data.models.IntervalSeries'>
'''


@schema
class Session(dj.Manual):
    # <class 'actions.models.Session'>
    # XXX: session_type table?
    definition = """
    -> subject.Subject
    session_number:             integer		# number
    session_start_time:         datetime	# start time
    ---
    session_end_time:           datetime	# end time
    session_type:		varchar(255)	# type
    -> reference.User
    """