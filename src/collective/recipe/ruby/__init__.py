# -*- coding: utf-8 -*-

from collective.recipe.cmmi import Recipe as Base
from zc.recipe.cmmi import system
import logging
import os
import os.path


class Recipe(Base):

    def __init__(self, buildout, name, options):
        super(Recipe, self).__init__(buildout, name, options)


    def install(self): 
        logger = logging.getLogger(self.name)
        logger.info("Install Ruby via CMMI")
        super(Recipe, self).install()

        gems = self.options.get('gems', [])
        gems = gems.splitlines()
        if gems:
            bin_dir = os.path.join(self.options['location'], 'bin')

            logger.info('Install Ruby Gems: {gems}'.format(gems=' '.join(gems)))
            if os.environ.get('https_proxy'):
                system('{path}/gem install --http-proxy={proxy} --source={source} {gems} '.format(path=bin_dir,gems=' '.join(gems),proxy=os.environ['https_proxy'],source='https://rubygems.org/'))
            #' --http-proxy=https://webscan-lb.verwaltung.uni-muenchen.de:8443 --source=https://rubygems.org/'
            elif os.environ.get('http_proxy'):
                system('{path}/gem install --http-proxy={proxy} --source={source} {gems} '.format(path=bin_dir,gems=' '.join(gems),proxy=os.environ['http_proxy'],source='http://rubygems.org/'))
            #' --http-proxy=https://webscan-lb.verwaltung.uni-muenchen.de:8443 --source=https://rubygems.org/'
            else:
                system('{path}/gem install {gems}'.format(path=bin_dir,gems=' '.join(gems)))
            #' --http-proxy=https://webscan-lb.verwaltung.uni-muenchen.de:8443 --source=https://rubygems.org/'