$(document).ready(function () {
    function fetchQuote() {
        // バックエンドから名言を取得するAPIエンドポイントにリクエストを送信します。
        // このURLは、Flaskアプリケーションが実装された後に適切なものに変更してください。
        const apiUrl = "http://127.0.0.1:5000/api/random_quote";

        $.getJSON(apiUrl, function (data) {
            const quote = data.quote;
            $("#quote").text(quote);
        });
    }

    fetchQuote();

    $("#generateButton").click(function () {
        fetchQuote();
    });
});
