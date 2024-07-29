#!/usr/bin/node
$(document).ready(function () {
    $('DIV#toggle_header').click(function () {
      if ($(this).hasClass('red')) {
        $(this).removeClass('red');
        $(this).addClass('green');
      } else {
        $(this).removeClass('green');
        $(this).addClass('red');
      }
    });
  });
