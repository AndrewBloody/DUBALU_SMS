# -*- coding: utf-8 -*-
"""
Dubalu Framework
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:author: Dubalu Framework Team. See AUTHORS.
:copyright: Copyright (c) 2013-2014, deipi.com LLC. All Rights Reserved.
:license: See LICENSE for license details.

"""
from __future__ import absolute_import, unicode_literals

from django_assets import Bundle

from . import Bundles


class Jsrsasign(Bundles):
    """
    Jsrsasign (RSA-Sign JavaScript Library) is an opensource free pure JavaScript
    cryptographic library supports RSA/RSAPSS/ECDSA/DSA signing/validation,
    ASN.1, PKCS#1/5/8 private/public key, X.509 certificate and CRL.

    [http://kjur.github.io/jsrsasign/]
    [https://code.google.com/p/crypto-js/]

    """
    # Some files (cryptojs) where not bundled in jsrsasign,
    # those were taken from CryptoJS v3.1.2
    js = Bundle(
        # cryptojs
        ########################################
        'src/js/cryptography/cryptojs/core.js',  # It has fix in cryptojs-312-core-fix.js
        'src/js/cryptography/cryptojs/x64-core.js',
        'src/js/cryptography/cryptojs/hmac.js',  # used by pbkdf2 (PBES2)
        # 'src/js/cryptography/cryptojs/sha256.js',
        # 'src/js/cryptography/cryptojs/sha224.js',
        # 'src/js/cryptography/cryptojs/sha512.js',
        # 'src/js/cryptography/cryptojs/sha384.js',
        'src/js/cryptography/cryptojs/md5.js',
        'src/js/cryptography/cryptojs/enc-base64.js',
        'src/js/cryptography/cryptojs/cipher-core.js',
        'src/js/cryptography/cryptojs/aes.js',  # optional (for decryption of AES)
        'src/js/cryptography/cryptojs/tripledes.js',
        'src/js/cryptography/cryptojs/sha1.js',
        # 'src/js/cryptography/cryptojs/ripemd160.js',
        'src/js/cryptography/cryptojs/pbkdf2.js',  # used for PBES2 (for encrypted DER files)

        # asmCrypto.js
        'src/js/cryptography/asmCrypto/base.js',
        'src/js/cryptography/asmCrypto/utils.js',
        'src/js/cryptography/asmCrypto/exports.js',
        'src/js/cryptography/asmCrypto/sha1/sha1.js',
        'src/js/cryptography/asmCrypto/sha1/sha1.asm.js',
        'src/js/cryptography/asmCrypto/sha1/exports.js',
        'src/js/cryptography/asmCrypto/hmac/hmac.js',
        'src/js/cryptography/asmCrypto/hmac/hmac-sha1.js',
        'src/js/cryptography/asmCrypto/hmac/exports.js',
        'src/js/cryptography/asmCrypto/pbkdf2/pbkdf2.js',
        'src/js/cryptography/asmCrypto/pbkdf2/pbkdf2-hmac-sha1.js',
        'src/js/cryptography/asmCrypto/pbkdf2/exports.js',

        # ext
        ########################################
        'src/js/cryptography/jsrsasign/ext/slim-yahoo.js',
        'src/js/cryptography/jsrsasign/ext/base64.js',
        'src/js/cryptography/jsrsasign/ext/jsbn.js',
        'src/js/cryptography/jsrsasign/ext/jsbn2.js',
        # 'src/js/cryptography/jsrsasign/ext/prng4.js',
        # 'src/js/cryptography/jsrsasign/ext/rng.js',
        'src/js/cryptography/jsrsasign/ext/rsa.js',
        'src/js/cryptography/jsrsasign/ext/rsa2.js',
        # 'src/js/cryptography/jsrsasign/ext/ec.js',
        # 'src/js/cryptography/jsrsasign/ext/ec-patch.js',

        # jsrsasign
        ########################################
        # 'src/js/cryptography/jsrsasign/asn1-1.0.js',
        'src/js/cryptography/jsrsasign/asn1hex-1.1.js',
        # 'src/js/cryptography/jsrsasign/asn1x509-1.0.js',
        # 'src/js/cryptography/jsrsasign/base64x-1.1.js',
        'src/js/cryptography/jsrsasign/crypto-1.1.js',
        # 'src/js/cryptography/jsrsasign/ecdsa-modified-1.0.js',
        # 'src/js/cryptography/jsrsasign/ecparam-1.0.js',
        # 'src/js/cryptography/jsrsasign/dsa-modified-1.0.js',
        'src/js/cryptography/jsrsasign/pkcs5pkey-1.0.js',
        'src/js/cryptography/jsrsasign/keyutil-1.0.js',
        'src/js/cryptography/jsrsasign/rsapem-1.1.js',
        'src/js/cryptography/jsrsasign/rsasign-1.2.js',
        'src/js/cryptography/jsrsasign/x509-1.1.js',
    )
