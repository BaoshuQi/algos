"""add domains to a dict"""

class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        dict = {}
        ret = []
        for s in cpdomains:
            c, domain = s.split(" ")
            subs = domain.split(".")
            for i in range (0, len(subs)):
                k = ".".join(subs[i:])
                if k in dict:
                    dict[k] += int(c)
                else:
                    dict[k] = int(c)
        for k in dict:
            ret.append(str(dict[k]) + " " + k)
        return ret


print(Solution.subdomainVisits(Solution(),["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))