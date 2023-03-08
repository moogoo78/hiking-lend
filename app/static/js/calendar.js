const DateTime = easepick.DateTime;

fetch('/api/v1/calendar/lended-dates')
  .then( r => r.json())
  .then( resp => {
    createCalendar(resp.booked_full, resp.booked_some);
  });

const createCalendar = (lockedDays, maybeDays) => {

  const bookedDates= lockedDays.map(d => {
      if (d instanceof Array) {
        const start = new DateTime(d[0], 'YYYY-MM-DD');
        const end = new DateTime(d[1], 'YYYY-MM-DD');
        return [start, end];
      }
      return new DateTime(d, 'YYYY-MM-DD');
      });

  console.log(lockedDays, maybeDays);

  const picker = new easepick.create({
    element: document.getElementById('datepicker'),
    calendars: 2,
    grid: 2,
    inline: true,
    css: [
      "/static/css/easepick.css",
      "/static/css/calendar-pick.css",
      'https://easepick.com/css/demo_prices.css',
    ],
    plugins: ['RangePlugin', 'LockPlugin'],
    RangePlugin: {
      tooltipNumber(num) {
        return num - 1;
      },
      locale: {
        one: '天',
        other: '天',
      },
    },
    LockPlugin: {
      minDate: new Date(),
      minDays: 2,
      inseparable: true,
      filter(date, picked) {
        if (picked.length === 1) {
          const incl = date.isBefore(picked[0]) ? '[)' : '(]';
          return !picked[0].isSame(date, 'day') && date.inArray(bookedDates, incl);
        }
        return date.inArray(bookedDates, '[]');
      },
    },
    setup(picker) {
      picker.on('view', (evt) => {
        const { view, date, target } = evt.detail;
        const d = date ? date.format('YYYY-MM-DD') : null;
        if (view === 'CalendarDay' && maybeDays.indexOf(d) >= 0) {
          target.classList.add('maybe');
        }
      });
    }
  });
}
