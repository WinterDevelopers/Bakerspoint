console.log('Bakerspoint')

let footer_img = document.querySelectorAll(".footer-img")

for(let a = 0; a < footer_img.length; a++){

    footer_img[a].addEventListener("click", function(){
        footer_img[a].className ='rotate-90'
    })
}

console.log('done!!')