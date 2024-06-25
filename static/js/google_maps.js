// Google Maps API Initialization
;(function (g) {
  var h,
    a,
    k,
    p = 'The Google Maps JavaScript API',
    c = 'google',
    l = 'importLibrary',
    q = '__ib__',
    m = document,
    b = window
  b = b[c] || (b[c] = {})
  var d = b.maps || (b.maps = {}),
    r = new Set(),
    e = new URLSearchParams(),
    u = () =>
      h ||
      (h = new Promise(async (f, n) => {
        await (a = m.createElement('script'))
        e.set('libraries', [...r] + '')
        for (k in g)
          e.set(
            k.replace(/[A-Z]/g, (t) => '_' + t[0].toLowerCase()),
            g[k],
          )
        e.set('callback', c + '.maps.' + q)
        a.src = `https://maps.${c}apis.com/maps/api/js?` + e
        d[q] = f
        a.onerror = () => (h = n(Error(p + ' could not load.')))
        a.nonce = m.querySelector('script[nonce]')?.nonce || ''
        m.head.append(a)
      }))
  d[l]
    ? console.warn(p + ' only loads once. Ignoring:', g)
    : (d[l] = (f, ...n) => r.add(f) && u().then(() => d[l](f, ...n)))
})({
  key: googleMapsApiKey,
  v: 'weekly',
})

document.addEventListener('DOMContentLoaded', async function () {
  const postsContainer = document.getElementById('posts-container')
  const googleMapsMapId = postsContainer.dataset.googleMapsMapId

  if (!googleMapsMapId) {
    console.error('Google Maps Map ID is not defined.')
    return
  }

  async function initializeMaps() {
    const { AdvancedMarkerElement } = await google.maps.importLibrary('marker')

    document.querySelectorAll('.map-container').forEach((mapElement, index) => {
      var lat = parseFloat(mapElement.dataset.lat)
      var lng = parseFloat(mapElement.dataset.lng)
      var location = { lat: lat, lng: lng }

      var map = new google.maps.Map(mapElement, {
        zoom: 14,
        center: location,
        mapId: googleMapsMapId,
      })

      new AdvancedMarkerElement({
        position: location,
        map: map,
      })
    })
  }

  initializeMaps()

  let page = 2
  const loadMoreButton = document.getElementById('load-more')
  if (loadMoreButton) {
    loadMoreButton.addEventListener('click', function () {
      fetch(`?page=${page}`, {
        headers: {
          'X-Requested-With': 'XMLHttpRequest',
        },
      })
        .then((response) => response.json())
        .then((data) => {
          if (data.posts) {
            postsContainer.insertAdjacentHTML('beforeend', data.posts)
            page += 1
            initializeMaps() // Reinitialize maps for new posts
            if (!data.has_next) {
              loadMoreButton.style.display = 'none'
            }
          }
        })
        .catch((error) => console.error('Error:', error))
    })
  }
})
