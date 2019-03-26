import scala.math.min
import scala.math.max

object Solution {
    def maxArea(height: Array[Int]): Int = {
        var m : Int = 0
        var left : Int = 0
        var right : Int= height.length -1
        while(left < right){
            var l : Int = height(left)
            var r: Int = height(right)
            m = max(m, (right - left) * min(l, r))
            if(r> l){
                left +=1
            }else{
                right -=1
            }
        }
        return m
    }
}