/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeNthFromEnd(head *ListNode, n int) *ListNode {
    t := head
    sum := 1
    for t.Next != nil{
        sum += 1
        t = t.Next
    }

    index := sum - n
    if index == 0{
        return head.Next
    }
    t = head
    for i := 1; i < index; i ++{
        t = t.Next
    }
    if t.Next.Next != nil{
        t.Next = t.Next.Next
    }else{
        t.Next = nil
    }
    return head
}
