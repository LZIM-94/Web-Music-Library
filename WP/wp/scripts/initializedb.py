import os
import sys
import transaction

from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from pyramid.scripts.common import parse_vars

from ..models import (
    DBSession,
    Genre,
	Music,
    Base,
    )


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    with transaction.manager:
		
		model2 = Genre(id = 0,name='HipHop', info='Nigger ma fucker',year_of_found = 1990)
		DBSession.add(model2)
		
		model = Genre(id = 1,name='GlitchHop', info='Nu vaaassheee',year_of_found = 2014, parent_genre = model2)
		DBSession.add(model)

                model3 = Genre(id = 2,name='Grime', info='Zhostkiy rap',year_of_found = 2006, parent_genre = model2)
		DBSession.add(model3)

                model4 = Genre(id = 3,name='Dark Grime', info='Tyomniy Zhostkiy rap',year_of_found = 2009, parent_genre = model3)
		DBSession.add(model4)
		
		music1 = Music(author = 'Simplex_Method', title = 'Of Literal Data', year = 2015,genre =  model3)
		DBSession.add(music1)
