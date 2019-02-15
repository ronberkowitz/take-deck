async function sendGetRequest(url) {
    const Http = new XMLHttpRequest();

    Http.open("GET", url);
    Http.send();
    Http.onreadystatechange = (e) => {
        return Http.responseText
    }
}

export default sendGetRequest;
