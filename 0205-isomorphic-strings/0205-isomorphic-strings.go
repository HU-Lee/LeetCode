func isIsomorphic(s string, t string) bool {
    s_dic := make(map[byte]byte)
    t_dic := make(map[byte]byte)
    for i, _ := range(t) {
        l1 := t[i]
        l2 := s[i]
        if val, ok := t_dic[l1]; !ok {
            t_dic[l1] = l2 
        } else {
            if val != l2 {
                return false
            } 
        }
        if val, ok := s_dic[l2]; !ok {
            s_dic[l2] = l1 
        } else {
            if val != l1 {
                return false
            } 
        }
    }
    return true
}