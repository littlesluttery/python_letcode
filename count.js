

function accAdd(arg1, arg2)
{
    var r1, r2, m;
    try {r1 = arg1.toString().split(".")[1].length} catch (e) {r1 = 0}
    try {r2 = arg2.toString().split(".")[1].length} catch (e) {r2 = 0}
    m = Math.pow(10, Math.max(r1, r2))
    var num = (arg1 * m + arg2 * m) / m
    return  num.toFixed(2)
}



Number.prototype.add = function (arg) {
                return accAdd(arg, this);
}
var  a = 1.1
var b = 2.22
console.log(Number(a).add(Number(b)));