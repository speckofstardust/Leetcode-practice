class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encodedStr=""
        for s in strs:
            l=len(s)
            encodedStr+=str(l)+"#"+s
        return encodedStr
    

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decodedStrs=[]
        i=0
        while(i<len(s)):
            j=i
            while(s[j]!="#"):
                j+=1
            length=int(s[i:j])
            str=s[j+1:j+1+length]
            decodedStrs.append(str)
            i=j+1+length
        return decodedStrs
