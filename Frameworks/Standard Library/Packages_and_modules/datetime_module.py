import datetime
import pytz
# # main module working with dates in time

# # https://www.programiz.com/python-programming/datetime/strftime

# print(datetime.time)
begin_time = datetime.datetime(2021, 5, 28, 14, 34)
end_time = datetime.datetime(2021, 5, 28, 23, 38)
total_time = end_time - begin_time
print(begin_time)
print(end_time)
print(total_time.total_seconds() / 3600)




# print(type(begin_time))
# a = str(begin_time)
# print(type(a))



# now = datetime.datetime.now()
# t2 = datetime.datetime(2021, 1, 20, 12, 3)
# time_now = now.time()
# time_then = t2.time()

# a = now - t2
# print(a.total_seconds() / 3600)










# # very important to learn to use this module
# # almost every app will interact with datetime

# # understand difference between naive and aware datetimes
# # naive dates - don't have information to determine things like timezones, DST etc...
# # but they are easier to work with if you don't need that level of detail
# # but a lot of the times you do -- that is when you use aware datetimes


# # naive dates
# d = datetime.date(2016, 7, 24)
# # be sure to pass integers for days and months with no 0
# print(d)

# tday = datetime.date.today()
# print(tday.year)
# print(tday.day)
# print(tday.weekday())
# # just two different formats, weekday counts monday as 0 and sunday as 6
# print(tday.isoweekday())
# # isoweekday counts monday as 1 and sunday as 7

# tdelta = datetime.timedelta(days=7)

# print(tday + tdelta)
# # this calculates 7 days from now, also works for subtraction
# print(tday - tdelta)
# # this prints the day that was one week ago from now

# # when we add or subtract a timedelta object from a date;
# # we are returned with another date that corresponds the new date;
# # whereas, when we abb or subtract two date objects from each other
# # we are returned with a timedelta object
# # date2 = date1 + timedelta
# # timedelta = date1 + date2

# # calculating birthday;
# print('yh')
# bd = datetime.date(2021, 5, 1)
# dob = datetime.date(1997, 5, 1)
# days_until_birtday = bd-tday
# time_i_been_alive = tday-dob
# times_like_these = datetime.datetime.now()


# # print(days_until_birtday.total_seconds())
# # print(time_i_been_alive)


# ### datetime time ###
# # with datetime.time -- we work with hours, minutes, seconds and micro seconds.
# # so it does not include year, month or the day.
# # by default does not have timezone, and therefore still naive.

# t = datetime.time(9, 30, 45, 10000)
# print(t)
# # like datetime.date -- we can access the values individually like...
# print(t.hour)
# print(t.minute)

# # this is rarely used separately, though it has SOME use cases;
# # because you need to usually know the date as well for it to be useful.


# ### datetime.datetime ###
# # this gives us access to EVERYTHING

dt = datetime.datetime(2016, 7, 26, 12, 13, 30, 100000)
# print(dt)
# print(dt.time())
# print(dt.date())
# # remember for a datetime object, the time() and date() are getter functions.
# print(dt.minute)
# # you can also add or subtract a tdelta onto a datetime object just like a date object
# # you can also use a duration of hours minutes in the timedelta object
# # whereas in the date object you can only add or subtract days.


tdelta2 = datetime.timedelta(days=3)
print(dt)
print(dt + tdelta2)


# dt_tday = datetime.datetime.today()
# dt_now = datetime.datetime.now()
# dt_utcnow = datetime.datetime.utcnow()

# print(dt_tday)
# # returns current local datetime with timezone of None
# print(dt_now)
# # returns current local datetime with an option for the timezone
# print(dt_utcnow)
# print("HERE!!")
# # this gives us the utc time now, but the tzinfo is still set to None
# # therefore, it is still a naive time.






# ### timezones ###
# # pytz, third party package, comes installed with
# # pytz is recommended in python library instead of timezone class;
# # more useful
# # recommended to always use UTC in timezones.

# print('\n\n\n')

# #dt3 = datetime.datetime(2010, 5, 16, 22, 43, 45, tzinfo=pytz.UTC)
# # this is the syntax for added the tzinfo;
# # also to note these are args, and kwarg.
# #print(dt3)
# # now the timezone has +00:00 at the end
# # this is the UTC offset.

# dt_now_utc = datetime.datetime.now(tz=pytz.UTC)
# print(dt_now_utc)
# #dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
# #print(dt_utcnow)
# # the above two are pretty much the same.
# # dt_now, is slightly easier to read, and Corey uses it.

# ## switching to a diff timezone ##
# dt_mtn = dt_now_utc.astimezone((pytz.timezone('US/Mountain')))
# print(dt_mtn)
# # here we took a timezone aware datetime object -- dt_now_utc
# # and we converted that to Mountain time
# # -06:00 mountain time, UTC offset.
# # pytz has a large list of timezones to select from

# # to see all the timezone code in the pytz module...
# # for tz in pytz.all_timezones:
# #    print(tz)


# ###
# # making naive datetime aware datetime
# dt5 = datetime.datetime.now()
# dt_east = dt5.astimezone(pytz.timezone('US/Eastern'))
# print(dt_east)
# # in python 3.6 and onwards;
# # this is no longer an error and astimezone CAN be applied to naive datetime instances that are presumed to represent
# # system local time.
# # whereas in older versions than 3.6, this would ahve raised an error.


# ## displaying datetime ##
# print(dt_east.isoformat())
# # iso is the default and most used, you will use this most the time
# # but you may want to use different ones from time to time
# # you can look at the python documentation for the strf format code.
# print(dt_east.strftime('%B %d, %Y'))


# dt_str = 'May 16, 2020'
# # in its current form, this is just a string.
# # and as just a string, it cannot perform any datetime methods
# # so I need to convert it into a datetime object.
# # to convert it into a datetime;
# dt6 = datetime.datetime.strptime(dt_str, '%B %d, %Y')
# print(dt6)

# # You can use str format code to convert datetime objects into a string format
# # and string formats in specific formats (depending on format code) to convert strings into datetime objects.

