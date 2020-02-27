'use script';

class Clock {
    constructor(options) {
        // options = {
        //     dayId: 'selectorName',
        //     monthId: 'selectorName',
        //     yearId: 'selectorName',
        //     hoursId: 'selectorName',
        //     minutesId: 'selectorName',
        //     timeZoneOffset: +8.00
        // }
        this.day_selector = document.getElementById(options.dayId);
        this.month_selector = document.getElementById(options.monthId);
        this.year_selector = document.getElementById(options.yearId);
        this.hours_selector = document.getElementById(options.hoursId);
        this.minutes_selector = document.getElementById(options.minutesId);

        // посчитаем и выставим часовой пояс пользователя,
        // пример: timeZoneOffset = +8.00
        let d = new Date();
        let tzDifference = options.timeZoneOffset * 60 + d.getTimezoneOffset();
        this.offset = tzDifference * 60 * 1000;

        this.month = [
            'января',
            'февраля',
            'марта',
            'апреля',
            'мая',
            'июня',
            'июля',
            'августа',
            'сентября',
            'октября',
            'ноября',
            'декабря',
        ]
    }

    render() {
        let date = new Date(new Date().getTime() + this.offset);

        if (this.hours_selector != null) {
            let hours = date.getHours();
            if (hours < 10) hours = '0' + hours;

            if (this.hours_selector.innerText !== '' + hours) {
                this.hours_selector.innerText = hours;
            }
        }

        if (this.minutes_selector != null) {
            let minutes = date.getMinutes();
            if (minutes < 10) minutes = '0' + minutes;

            if (this.minutes_selector.innerText !== '' + minutes) {
                this.minutes_selector.innerText = minutes;
            }
        }

        if (this.day_selector != null) {
            let day = date.getDate();

            if (this.day_selector.innerText !== '' + day) {
                this.day_selector.innerText = day;
            }
        }

        if (this.month_selector != null) {
            let month_index = date.getMonth();
            if (this.month_selector.innerText !== this.month[month_index]) {
                this.month_selector.innerText = this.month[month_index];
            }
        }

        if (this.year_selector != null) {
            let year = date.getFullYear();
            if (this.year_selector.innerText !== '' + year) {
                this.year_selector.innerText = year;
            }
        }
    }

    stop() {
        clearInterval(this.timer);
    }

    start() {
        this.render();
        this.timer = setInterval(() => this.render(), 1000)
    }
}
