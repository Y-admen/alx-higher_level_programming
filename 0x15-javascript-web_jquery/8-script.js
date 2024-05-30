$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
  const movies = data.results;
  const $movieList = $('UL#list_movies');

  for (const movie of movies) {
    const $movieItem = $('<li></li>').text(movie.title);
    $movieList.append($movieItem);
  }
});
