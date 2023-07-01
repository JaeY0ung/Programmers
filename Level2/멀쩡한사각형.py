def solution(w,h):
    def gcd(w, h):
        if h == 0:
            return w
        return gcd(h, w % h)
    return w * h - w - h + gcd(w-h, h)