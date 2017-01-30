$(document).ready(function () {

    initCalculator($('#calculator-running form'));
    initCalculator($('#calculator-swimming form'));

    $(window).on('hashchange', function() {
        initContentByUrl();
    });

    initContentByUrl();
});

function initContentByUrl()
{
    var hash = window.location.hash;

    var elementToShow = $('#calculator-container > [data-routing-code="'+hash+'"]');

    if ($(elementToShow).length > 0) {
        $('#calculator-container > .panel').addClass('hidden');
        $(elementToShow).removeClass('hidden');

        $('#main-nav li').each(function (key, element) {
            if ($(element).find('a').attr('href') == hash) {
                $(element).addClass('active');
            } else {
                $(element).removeClass('active');
            }
        });
    }
}

function initCalculator(form)
{
    $(form).on('submit', function (e) {
        e.preventDefault();

        var submittedForm = $(this);

        $(submittedForm).find('.has-error').each(function (index, element) {
            $(element).removeClass('has-error');
        });

        $(submittedForm).find('.help-block.validMessage').html('');

        $.post($(this).attr('action'), $(this).serialize(), function (response) {

            if (response.result == false) {
                $.each(response.errors, function (errorField, errorValue) {
                    var field = $(submittedForm).find('[name=' + errorField + ']');
                    var errorBlock = $(field).parent().parent().find('.help-block.validMessage');
                    var controlGroup = $(field).parents('.control-group');

                    $(controlGroup).addClass('has-error');
                    $(errorBlock).html(errorValue[0]);
                });
            } else {

                $(submittedForm).attr('data-result-is-calculated', '1');

                if (typeof response.result_data.time !== 'undefined') {
                    $(submittedForm).find('[name=time_hours]').val(response.result_data.time.hours);
                    $(submittedForm).find('[name=time_minutes]').val(response.result_data.time.minutes);
                    $(submittedForm).find('[name=time_seconds]').val(response.result_data.time.seconds);
                }
                else if (typeof response.result_data.tempo !== 'undefined') {
                    $(submittedForm).find('[name=tempo_minutes]').val(response.result_data.tempo.minutes);
                    $(submittedForm).find('[name=tempo_seconds]').val(response.result_data.tempo.seconds);
                }
                else if (typeof response.result_data.distance !== 'undefined') {
                    $(submittedForm).find('[name=distance]').val(response.result_data.distance);
                }
            }

        });

        return false;

    });

    var calculator = new Calculator(form);
    calculator.setFieldsState();

    $(form).find('button[name=reset]').on('click', function (e) {
        $(form).removeAttr('data-result-is-calculated');
        $(form).find('input').each(function(index, element) {
            $(element).val('');
        });
        calculator.setFieldsState();
    });

    $(form).find('input').on('keyup', function (e) {
        if ($(form).attr('data-result-is-calculated') !== '1') {
            calculator.setFieldsState();
        }
    });
}

function Calculator(form) {
    this.form = form;
    this.distanceSelector = 'input[name=distance]';
    this.tempoMinutesSelector = 'input[name=tempo_minutes]';
    this.tempoSecondsSelector = 'input[name=tempo_seconds]';
    this.timeHoursSelector = 'input[name=time_hours]';
    this.timeMinutesSelector = 'input[name=time_minutes]';
    this.timeSecondsSelector = 'input[name=time_seconds]';

    this.setFieldsState = function () {

        var hasDistance = this.hasDistance();
        var hasTempo = this.hasTempo();
        var hasTime = this.hasTime();

        this.setDisableAttributeToEditForTime(hasDistance && hasTempo);
        this.setDisableAttributeToEditForTempo(hasDistance && hasTime);
        this.setDisableAttributeToEditForField(this.distanceSelector, hasTempo && hasTime);
    };

    this.getField = function (selector) {
        return $(this.form).find(selector);
    };

    this.hasDistance = function () {
        return $.trim(this.getField(this.distanceSelector).val()) != '';
    }

    this.hasTime = function () {
        var hasTimeHours = $.trim(this.getField(this.timeHoursSelector).val()) != '';
        var hasTimeMinutes = $.trim(this.getField(this.timeMinutesSelector).val()) != '';
        var hasTimeSeconds = $.trim(this.getField(this.timeSecondsSelector).val()) != '';

        return hasTimeHours || hasTimeMinutes || hasTimeSeconds;
    }

    this.hasTempo = function () {
        var hasTempoMinutes = $.trim(this.getField(this.tempoMinutesSelector).val()) != '';
        var hasTempoSeconds = $.trim(this.getField(this.tempoSecondsSelector).val()) != '';

        return hasTempoMinutes || hasTempoSeconds;
    }

    this.setDisableAttributeToEditForTime = function (isDisabled) {
        this.setDisableAttributeToEditForField(this.timeHoursSelector, isDisabled);
        this.setDisableAttributeToEditForField(this.timeMinutesSelector, isDisabled);
        this.setDisableAttributeToEditForField(this.timeSecondsSelector, isDisabled);
    }

    this.setDisableAttributeToEditForTempo = function (isDisabled) {
        this.setDisableAttributeToEditForField(this.tempoMinutesSelector, isDisabled);
        this.setDisableAttributeToEditForField(this.tempoSecondsSelector, isDisabled);
    }

    this.setDisableAttributeToEditForField = function (selector, isDisabled) {
        this.getField(selector).prop('disabled', isDisabled);
    }
}
