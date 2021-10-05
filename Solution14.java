/*
给定一个非负整数 N，找出小于或等于 N 的最大的整数，同时这个整数需要满足其各个位数上的数字是单调递增。

（当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。）
输入: N = 10
输出: 9
暴力法：超时。
 */
public class Solution14 {
    public static void main(String[] args) {
        int i = monotoneIncreasingDigits(853567367);
        System.out.println(i);

    }
    public static int monotoneIncreasingDigits(int n){
        for (int i = n; i >0 ; i--) {
            if (checkNum(i)) return i;
        }
        return 0;
    }

    private static boolean checkNum(int num) {
        int max=10;
        while(num != 0){
            int t = num%10;
            if (max>=t) max=t;
            else return false;
            num = num/10;

        }
        return true;
    }
}
