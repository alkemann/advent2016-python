import unittest
from day_seven.protocol import has_tls, has_ssl


# noinspection SpellCheckingInspection
class ProtocolTestCase(unittest.TestCase):
    def test_tls(self):
        # supports TLS (abba outside square brackets).
        self.assertTrue(has_tls("abba[mnop]qrst"))

        # does not support TLS (bddb is within square brackets, even though xyyx is outside square brackets).
        self.assertFalse(has_tls("abcd[bddb]xyyx"))

        # does not support TLS (aaaa is invalid; the interior characters must be different).
        self.assertFalse(has_tls("aaaa[qwer]tyui"))

        # supports TLS (oxxo is outside square brackets, even though it's within a larger string).
        self.assertTrue(has_tls("ioxxoj[asdfgh]zxcvbn"))

    def test_ssl(self):
        self.assertFalse(has_ssl("rxpusykufgqujfe[rypwoorxdemxffui]cvvcufcqmxoxcphp[witynplrfvquduiot]vcysdcsowcxhphp[gctucefriclxaonpwe]jdprpdvpeumrhokrcjt"))
        # supports SSL (aba outside square brackets with corresponding bab within square brackets).
        self.assertTrue(has_ssl("aba[bab]xyz"))
        # does not support SSL (xyx, but no corresponding yxy).
        self.assertFalse(has_ssl("xyx[xyx]xyx"))
        # supports SSL (eke in supernet with corresponding kek in hypernet; the aaa sequence is not related, because the interior character must be different).
        self.assertTrue(has_ssl("aaa[kek]eke"))
        # supports SSL (zaz has no corresponding aza, but zbz has a corresponding bzb, even though zaz and zbz overlap).
        self.assertTrue(has_ssl("zazbz[bzb]cdb"))
