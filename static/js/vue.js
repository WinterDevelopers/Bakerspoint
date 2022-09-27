const url = 'api/'

fetch(url)
.then(data => {
    return data.json()
})
.then(post => {
    console.log(post.name)
})