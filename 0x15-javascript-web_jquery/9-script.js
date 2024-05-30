$(document).ready(function() {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data) {
    const regex = /bonjour/i;
    if (regex.test(data)) {
      $('div#hello').text(data.trim());
    }
  });
      });
      