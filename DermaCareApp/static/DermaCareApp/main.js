const eventBox = document.getElementById('event_date')
var table = document.getElementById('tbc')
const CountdownBox = document.getElementById('countdown')
const apps = document.getElementsByClassName('apps')
console.log(eventBox.textContent)
const eventDate = Date.parse(eventBox.textContent)
console.log(eventDate)

setInterval(()=>{
    const now = new Date().getTime()
    const diff = eventDate - now

    const d = Math.floor (eventDate/(1000*60*60*24) - (now/(1000*60*60*24)))
    const h = Math.floor ((eventDate/(1000*60*60) - (now/(1000*60*60)))%24)
    const m = Math.floor ((eventDate/(1000*60) - (now/(1000*60)))%60)
    const s = Math.floor ((eventDate/(1000) - (now/(1000)))%60)
    
    for(var i = 0;table.rows[i] ; i++){
        if(diff>0){
            CountdownBox.innerHTML = d + "d " + h + " : " + m + " : " + s + "s";
            }else{
            CountdownBox.innerHTML = "Expired";
        }
    }

}, 1000)

