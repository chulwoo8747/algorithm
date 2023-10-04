function solution(price) {
    var result = price;
    if (price >= 500000) {
        result = (price-price*0.2)
    }
    else if (price >= 300000 && price < 500000 ) {
        result = (price-price*0.1)
    }
    else if (price >= 100000 && price < 300000) {
        result = (price-price*0.05)
    }
    return Math.floor(result);
}