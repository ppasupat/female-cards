$(function () {

  var totalCards = MONSTERS.length + BACKROWS.length;
  var cardsPerPage = 12;
  var totalPages = Math.ceil(1. * totalCards / cardsPerPage);
  var currentPage;

  function displayPage(pageNum) {
    currentPage = pageNum;
    $('#page-number').text('Page ' + pageNum + ' / ' + totalPages);
    $('#content').empty();
    var from = (pageNum - 1) * cardsPerPage;
    var to = Math.min(totalCards, pageNum * cardsPerPage);
    for (var i = from; i < to; i++) {
      if (i < MONSTERS.length) {
        addMonster(MONSTERS[i]);
      } else {
        addBackrow(BACKROWS[i - MONSTERS.length]);
      }
    }
    $('#prev-button').prop('disabled', currentPage == 1);
    $('#next-button').prop('disabled', currentPage == totalPages);
  }

  function addMonster(x) {
    var frame = $('<a class=card target=_blank>').appendTo('#content')
      .attr('href', 'http://yugioh.wikia.com/wiki/' + x['English name'].replace(/ /g, '_'))
      .append($('<img>').attr('src', 'img/' + (+x.Password) + '.png'))
      .append($('<p class=eng>').text(x['English name']));
  }

  var addBackrow = addMonster;

  $('#prev-button').click(() => displayPage(currentPage - 1));
  $('#next-button').click(() => displayPage(currentPage + 1));
  $('#page-number').click(() => {
    var pageNum = prompt('Page number');
    if (!isNaN(+pageNum) && pageNum.length)
      displayPage(Math.max(1, Math.min(totalPages, +pageNum)));
  });

  $(document).keydown(function (event) {
    console.log(event);
    var c = event.key;
    if (c == "ArrowLeft" || c == "a") {
      if (!$('#prev-button').prop('disabled'))
        $('#prev-button').click();
    } else if (c == "ArrowRight" || c == "d") {
      if (!$('#next-button').prop('disabled'))
        $('#next-button').click();
    } else if (c == "g") {
      $('#page-number').click();
    }
  });

  displayPage(1);

});
