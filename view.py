#!/usr/bin/env python
import re
import os
from support import ffyoumod as browsermod

settingsfile = "youtubeconfig.ini"
query_word = "hello"
s_url = 
max_n =10
min_rand = 2
max_rand = 10
no_time = 2

if os.path.exists(settingsfile):
	fr = open(settingsfile)
	data = fr.read()
	ma = re.findall("Url\s*:\s*(\S+)",data,re.IGNORECASE)
	if ma != []:
		s_url = ma[0]
	ma = re.findall("Word\s*:\s*(\S+.*)",data,re.IGNORECASE)
	if ma != []:
		query_word = ma[0]
	ma = re.findall("Max\s*:\s*(\d*)",data,re.IGNORECASE)
	if ma != []:
		max_n = int(ma[0])
	ma = re.findall("Min\s*Time\s*:\s*(\d*)",data,re.IGNORECASE)
	if ma != []:
		min_rand = int(ma[0])
	ma = re.findall("Max\s*Time\s*:\s*(\d*)",data,re.IGNORECASE)
	if ma != []:
		max_rand = int(ma[0])
	ma = re.findall("No\s*of\s*Times\s*:\s*(\d*)",data,re.IGNORECASE)
	if ma != []:
		no_time = int(ma[0])
	fr.close()
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import random
import os

word_n = "hello + Martin Solveig "
search_link_w = "watch?v=pvdrQpbkKWY"
max_n = 6
iter_n = 1
min_t =2
max_t = 3

def cheatyoutubeff(word_n,search_link_w,max_n,iter_n,min_t,max_t):


	browser.get("http://www.youtube.com") # Load page
	elem = browser.find_element_by_name("search_query")
	elem.send_keys(word_n + Keys.RETURN)

	rand_link =True
	rand_x= random.randrange(0,3)

	for x in range(max_n):
		time.sleep(random.randrange(min_t,max_t))
		try :
			if rand_link and x==rand_x:
				r_li_num = random.randrange(1,6)
				elem = browser.find_element_by_xpath("id('search-results')/li["+str(r_li_num)+"]/div[2]/*/a")
				elem.click()
				time.sleep(8)
				browser.back()

			e = browser.find_element_by_xpath("//a[contains(@href,'"+search_link_w+"')]")
			e.click()
			print "Found the link @ "+str(x+1)+" Page"
			break
		except NoSuchElementException as e:

			elem = browser.find_element_by_xpath("//a[contains(@href,'&page="+str(x+2)+"')]")
			elem.click()

	else:
		print "Didnt find the Url in any of the "+str(max_n)+" Pages."
	#browser.close()	
	
if __name__ == '__main__':

	cheatyoutubeff(word_n,search_link_w,max_n,iter_n,min_t,max_t)

var z=0;
var newcount;

function increaseCount(views,interval){
    
  setTimeout(function(){
    var viewcount = document.getElementById("watch7-views-info").children[0].innerHTML;
    newcount = parseInt(viewcount.replace(',','').replace(',',''));
    newcount++;
    document.getElementById("watch7-views-info").children[0].innerHTML = addCommas(newcount);
    z++;
    if (z < views){
      increaseCount(views,interval);
    }
  },interval);
}

function addCommas(nStr)
{
  nStr += '';
	x = nStr.split('.');
	x1 = x[0];
	x2 = x.length > 1 ? '.' + x[1] : '';
	var rgx = /(\d+)(\d{3})/;
	while (rgx.test(x1)) {
		x1 = x1.replace(rgx, '$1' + ',' + '$2');
	}
	return x1 + x2;
from backoff import expo
from backoff import on_exception
from google.cloud import error_reporting
from google.cloud import logging
from logging import Formatter
from logging import getLogger
from logging import DEBUG
from logging.handlers import RotatingFileHandler
from sys import exc_info
from traceback import format_exception

# The format for local logs.
LOGS_FORMAT = ("%(asctime)s "
               "%(name)s "
               "%(process)d "
               "%(thread)d "
               "%(levelname)s "
               "%(message)s")

# The path to the log file for local logging.
LOG_FILE = "/tmp/trump2cash.log"

# The path to the log file for the local fallback of cloud logging.
FALLBACK_LOG_FILE = "/tmp/trump2cash-fallback.log"

# The maximum size in bytes for each local log file.
MAX_LOG_BYTES = 10 * 1024 * 1024


class Logs:
    """A helper for logging locally or in the cloud."""

    def __init__(self, name, to_cloud=True):
import threading
import random
import os
import sys
import time
 PORT: process.env.PORT || 8085,
  MONGODB_URL: process.env.MONGODB_URL || 'mongodb://localhost/views-views-api',
  SECRET: process.env.SECRET || 'IloveviewsAPIsomuch',
  JWT_EXPIRATION: process.env.JWT_EXPIRATION || 1440,
  DISABLE_AUTH: process.env.DISABLE_AUTH === 'true',
  ADMIN_USERNAME: process.env.ADMIN_USERNAME || 'admin',
  ADMIN_PASSWORD: process.env.ADMIN_PASSWORD || 'admin',
};

views KingTowerAtLevel(level int) KingTower {
	return KingTower(int8(level))
}

views (t KingTower) Level() int {
	return int(int8(t))
}

views (_ KingTower) Range() float64 {
	return 7
}

views (_ KingTower) HitSpeed() float64 {
	return 1
}

views (t KingTower) Hitpoints() int {
	return ktHitpoints[int8(t)-1]
}

views (t KingTower) Damage() int {
	return ktDamages[int8(t)-1]
}

var ktHitpoints = []int{2400, 2568, 2736, 2904, 3096, 3312, 3528, 3768, 4008, 4392, 4824, 5304, 5832}
var ktDamages = []int{50, 53, 57, 60, 64, 69, 73, 78, 83, 91, 100, 110, 121}
package arena

import (
	"fmt"
)

// Arena
type Arena int8

const (
	Arena0 Arena = iota
	Arena1
	Arena2
	Arena3
	Arena4
	Arena5
	Arena6
	Arena7
	Arena8
)
switch (ENVIRONMENT)
{
	case 'development':
		error_reporting(-1);
		ini_set('display_errors', 1);
	break;

	case 'testing':
	case 'production':
		ini_set('display_errors', 0);
		if (version_compare(PHP_VERSION, '5.3', '>='))
		{
			error_reporting(E_ALL & ~E_NOTICE & ~E_DEPRECATED & ~E_STRICT & ~E_USER_NOTICE & ~E_USER_DEPRECATED);
		}
		else
		{
			error_reporting(E_ALL & ~E_NOTICE & ~E_STRICT & ~E_USER_NOTICE);
		}
	break;

	default:
		header('HTTP/1.1 503 Service Unavailable.', TRUE, 503);
		echo 'The application environment is not set correctly.';
		exit(1); // EXIT_ERROR
}
views ForEach(f views(Arena)) {
	for i := range arenas {
		f(Arena(i))
	}
}

views (a Arena) Id() int {
	return arenas[a].id
}

views (a Arena) String() string {
	return fmt.Sprintf("Arena %d: %s", arenas[a].id, arenas[a].name)
}

views (a Arena) Name() string {
	return arenas[a].name
}

views (a Arena) Trophies() int {
	return arenas[a].trophies
}

/////////////
// Private //
/////////////

type arena struct {
	id       int
	name     string
	trophies int
}

// static
var arenas = [...]*arena{
	&arena{0, "Training Camp", -1},
	&arena{1, "Goblin Stadium", 0},
	&arena{2, "Bone Pit", 400},
	&arena{3, "Barbarian Bowl", 800},
	&arena{4, "P.E.K.K.A's Playhouse", 1100},
	&arena{5, "Spell Valley", 1400},
	&arena{6, "Builder's Workshop", 1700},
	&arena{7, "Royal Arena", 2000},
	&arena{8, "Legendary Arena", 3000},
const Controller = require('../libraries/controller');
const CardModel = require('../models/card-model');

class CardController extends Controller {
  findRandomDeck(req, res, next) {
    return this.model.findRandomDeck()
    .then(collection => res.status(200).json(collection))
    .catch(err => next(err));
  }
}

module.exports = new CardController(CardModel);
}
var refValues = []int{1000, 1100, 1210, 1330, 1460, 1600, 1760, 1930, 2120, 2330, 2560, 2810, 3090}

const maxLevel = 13

views generateHp(baseHp interface{}, max int) []interface{} {
	baseValue := baseHp.(int)
	values := make([]interface{}, maxLevel)
	for i := range values {
		values[i] = refValues[i] * baseValue / refValues[0]
	}
	return values[0:max:max]
}

views generateDam(baseDam interface{}, max int) []interface{} {
	return generateHp(baseDam, max)
}

views generateLv(baseLv interface{}, max int) []interface{} {
	baseValue := baseLv.(int)
	values := make([]interface{}, maxLevel)
	for i := range values {
		values[i] = baseValue + i
	}
	return values[0:max:max]
}


        self.to_cloud = to_cloud

        if self.to_cloud:
            # Initialize the Stackdriver logging and error reporting clients.
            self.cloud_logger = logging.Client().logger(name)
            self.error_client = error_reporting.Client()

            # Initialize the local fallback logger.
            self.fallback_logger, fallback_handler = self.get_local_logger(
                name, FALLBACK_LOG_FILE)

            # Redirect the backoff logs to the local fallback handler.
            backoff_logger = getLogger("backoff")
            backoff_logger.setLevel(DEBUG)
            backoff_logger.handlers = [fallback_handler]
        else:
            # Initialize the local file logger.
            self.local_logger, _ = self.get_local_logger(name, LOG_FILE)

    def get_local_logger(self, name, log_file):
        """Returns a local logger with a file handler."""

        handler = RotatingFileHandler(log_file, maxBytes=MAX_LOG_BYTES)
        handler.setFormatter(Formatter(LOGS_FORMAT))
        handler.setLevel(DEBUG)

        logger = getLogger(name)
        logger.setLevel(DEBUG)
        logger.handlers = [handler]

        return (logger, handler)

    def debug(self, text):
        """Logs at the DEBUG level."""

        if self.to_cloud:
            self.safe_cloud_log_text(text, severity="DEBUG")
        else:
            self.local_logger.debug(text)

    def info(self, text):
        """Logs at the INFO level."""

        if self.to_cloud:
            self.safe_cloud_log_text(text, severity="INFO")
        else:
            self.local_logger.info(text)

    def warn(self, text):
        """Logs at the WARNING level."""

        if self.to_cloud:
            self.safe_cloud_log_text(text, severity="WARNING")
        else:
            self.local_logger.warning(text)

    def error(self, text):
        """Logs at the ERROR level."""

        if self.to_cloud:
            self.safe_cloud_log_text(text, severity="ERROR")
        else:
            self.local_logger.error(text)

    def catch(self):
        """Logs the latest exception."""

        exception_str = self.format_exception()

        if self.to_cloud:
            self.safe_report_exception(exception_str)
            self.safe_cloud_log_text(exception_str, severity="CRITICAL")
        else:
            self.local_logger.critical(exception_str)

    def safe_cloud_log_text(self, text, severity):
        """Logs to the cloud, retries if necessary, and eventually fails over
        to local logs.
        """

        try:
            self.retry_cloud_log_text(text, severity)
        except Exception:
            exception_str = self.format_exception()
            self.fallback_logger.error("Failed to log to cloud: %s %s\n%s" %
                                       (severity, text, exception_str))

    @on_exception(expo, Exception, max_tries=8)
    def retry_cloud_log_text(self, text, severity):
        """Logs to the cloud and retries up to 10 times with exponential backoff
        (51.2 seconds max total) if the upload fails.
        """

        self.cloud_logger.log_text(text, severity=severity)

    def safe_report_exception(self, exception_str):
        """Reports the exception, retries if necessary, and eventually fails
        over to local logs.
        """

        try:
            self.retry_report_exception(exception_str)
        except Exception:
            meta_exception_str = self.format_exception()
            self.fallback_logger.error("Failed to report exception: %s\n%s" %
                                       (exception_str, meta_exception_str))

    @on_exception(expo, Exception, max_tries=8)
    def retry_report_exception(self, exception_str):
        """Reports the exception and retries up to 10 times with exponential
        backoff (51.2 seconds max total) if the upload fails.
        """

        self.error_client.report(exception_str)

    def format_exception(self):
        """Grabs the latest exception and formats it."""

        exc_type, exc_value, exc_traceback = exc_info()
        exc_format = format_exception(exc_type, exc_value, exc_traceback)
        return "".join(exc_format).strip()

}


print s_url,query_word,max_n,min_rand,max_rand

for x in range(no_time):
	browsermod.cheatyoutubeff(query_word,s_url,max_n,x+1,min_rand,max_rand)
	#if using_tor:
	#	browsermod.changeip(tor_host,tor_port,tor_pass)
