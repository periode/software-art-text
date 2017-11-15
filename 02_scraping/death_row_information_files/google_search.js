function submitQuery() {
  window.location = '/search_results.html?q=' + encodeURIComponent(document.getElementById('search_input').value);
  return false;
}