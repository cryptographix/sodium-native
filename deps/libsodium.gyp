{
    'targets': [
        {
            'target_name': 'libsodium',
            'variables': {
                'target_arch%': "<!(node -e \"console.log(require('os').arch())\")",
            },
            'type': 'static_library',
            'dependencies': [],
            'defines': [
                'SODIUM_STATIC',
                'HAVE_LIBM=1',
                '<!@(node ../makefile.js --defines)',
            ],
            'include_dirs': [
                'libsodium/src/libsodium/include/sodium',
            ],
            'xcode_settings': {
                'OTHER_CFLAGS': [
                        '-fPIC',
                        '-fwrapv',
                        '-fno-strict-aliasing',
                        '-fstack-protector-all',
                        '-Winit-self',
                        '-Wwrite-strings',
                        '-Wdiv-by-zero',
                        '-Wmissing-braces',
                        '-Wmissing-field-initializers',
                        '-Wno-sign-compare',
                        '-Wno-unused-const-variable',
                        '-g',
                        '-O2',
                        '-fvisibility=hidden',
                        '-Wno-missing-field-initializers',
                        '-Wno-missing-braces',
                        '-Wno-unused-function',
                        '-Wno-strict-overflow',
                        '-Wno-unknown-pragmas',
                        '<!@(node ../makefile.js --cflags)',
                ],
                'GCC_ENABLE_CPP_EXCEPTIONS': 'YES'
            },
            '!cflags': ['-fno-exceptions'],
            'cflags': [
                '-fexceptions',
                '-Winit-self',
                '-Wwrite-strings',
                '-Wdiv-by-zero',
                '-Wmissing-braces',
                '-Wmissing-field-initializers',
                '-Wno-sign-compare',
                '-Wno-unused-but-set-variable',
                '-g',
                '-O2',
                '-Wno-unknown-pragmas',
                '-Wno-missing-field-initializers',
                '-Wno-missing-braces',
                '<!@(node ../makefile.js --cflags)',
            ],
            'ldflags': [
                '-pie',
                '-Wl',
                '-z',
                'relro'
                '-z',
                'now'
                '-Wl',
                '-z',
                'noexecstack'
            ],

            'sources': [
              'libsodium/src/libsodium/sodium/core.c',
              'libsodium/src/libsodium/sodium/runtime.c',
              'libsodium/src/libsodium/sodium/utils.c',
              'libsodium/src/libsodium/sodium/version.c',
              'libsodium/src/libsodium/crypto_aead/aes256gcm/aesni/aead_aes256gcm_aesni.c',
              'libsodium/src/libsodium/crypto_aead/chacha20poly1305/sodium/aead_chacha20poly1305.c',
              'libsodium/src/libsodium/crypto_auth/crypto_auth.c',
              'libsodium/src/libsodium/crypto_auth/hmacsha256/auth_hmacsha256_api.c',
              'libsodium/src/libsodium/crypto_auth/hmacsha256/cp/hmac_hmacsha256.c',
              'libsodium/src/libsodium/crypto_auth/hmacsha256/cp/verify_hmacsha256.c',
              'libsodium/src/libsodium/crypto_auth/hmacsha512/auth_hmacsha512_api.c',
              'libsodium/src/libsodium/crypto_auth/hmacsha512/cp/hmac_hmacsha512.c',
              'libsodium/src/libsodium/crypto_auth/hmacsha512/cp/verify_hmacsha512.c',
              'libsodium/src/libsodium/crypto_auth/hmacsha512256/auth_hmacsha512256_api.c',
              'libsodium/src/libsodium/crypto_auth/hmacsha512256/cp/hmac_hmacsha512256.c',
              'libsodium/src/libsodium/crypto_auth/hmacsha512256/cp/verify_hmacsha512256.c',
              'libsodium/src/libsodium/crypto_box/crypto_box.c',
              'libsodium/src/libsodium/crypto_box/crypto_box_easy.c',
              'libsodium/src/libsodium/crypto_box/crypto_box_seal.c',
              'libsodium/src/libsodium/crypto_box/curve25519xsalsa20poly1305/box_curve25519xsalsa20poly1305_api.c',
              'libsodium/src/libsodium/crypto_box/curve25519xsalsa20poly1305/ref/after_curve25519xsalsa20poly1305.c',
              'libsodium/src/libsodium/crypto_box/curve25519xsalsa20poly1305/ref/before_curve25519xsalsa20poly1305.c',
              'libsodium/src/libsodium/crypto_box/curve25519xsalsa20poly1305/ref/box_curve25519xsalsa20poly1305.c',
              'libsodium/src/libsodium/crypto_box/curve25519xsalsa20poly1305/ref/keypair_curve25519xsalsa20poly1305.c',
              'libsodium/src/libsodium/crypto_core/curve25519/ref10/curve25519_ref10.c',
              'libsodium/src/libsodium/crypto_core/hchacha20/core_hchacha20.c',
              'libsodium/src/libsodium/crypto_core/hsalsa20/core_hsalsa20_api.c',
              'libsodium/src/libsodium/crypto_core/hsalsa20/ref2/core_hsalsa20.c',
              'libsodium/src/libsodium/crypto_core/salsa20/core_salsa20_api.c',
              'libsodium/src/libsodium/crypto_core/salsa20/ref/core_salsa20.c',
              'libsodium/src/libsodium/crypto_core/salsa2012/core_salsa2012_api.c',
              'libsodium/src/libsodium/crypto_core/salsa2012/ref/core_salsa2012.c',
              'libsodium/src/libsodium/crypto_core/salsa208/core_salsa208_api.c',
              'libsodium/src/libsodium/crypto_core/salsa208/ref/core_salsa208.c',
              'libsodium/src/libsodium/crypto_generichash/blake2/generichash_blake2_api.c',
              'libsodium/src/libsodium/crypto_generichash/blake2/ref/blake2b-compress-avx2.c',
              'libsodium/src/libsodium/crypto_generichash/blake2/ref/blake2b-compress-ref.c',
              'libsodium/src/libsodium/crypto_generichash/blake2/ref/blake2b-compress-sse41.c',
              'libsodium/src/libsodium/crypto_generichash/blake2/ref/blake2b-compress-ssse3.c',
              'libsodium/src/libsodium/crypto_generichash/blake2/ref/blake2b-ref.c',
              'libsodium/src/libsodium/crypto_generichash/blake2/ref/generichash_blake2b.c',
              'libsodium/src/libsodium/crypto_generichash/crypto_generichash.c',
              'libsodium/src/libsodium/crypto_hash/crypto_hash.c',
              'libsodium/src/libsodium/crypto_hash/sha256/cp/hash_sha256.c',
              'libsodium/src/libsodium/crypto_hash/sha256/hash_sha256_api.c',
              'libsodium/src/libsodium/crypto_hash/sha512/cp/hash_sha512.c',
              'libsodium/src/libsodium/crypto_hash/sha512/hash_sha512_api.c',
              'libsodium/src/libsodium/crypto_onetimeauth/crypto_onetimeauth.c',
              'libsodium/src/libsodium/crypto_onetimeauth/poly1305/donna/poly1305_donna.c',
              'libsodium/src/libsodium/crypto_onetimeauth/poly1305/onetimeauth_poly1305.c',
              'libsodium/src/libsodium/crypto_onetimeauth/poly1305/sse2/poly1305_sse2.c',
              'libsodium/src/libsodium/crypto_pwhash/argon2/argon2-core.c',
              'libsodium/src/libsodium/crypto_pwhash/argon2/argon2-encoding.c',
              'libsodium/src/libsodium/crypto_pwhash/argon2/argon2-fill-block-ref.c',
              'libsodium/src/libsodium/crypto_pwhash/argon2/argon2-fill-block-ssse3.c',
              'libsodium/src/libsodium/crypto_pwhash/argon2/argon2.c',
              'libsodium/src/libsodium/crypto_pwhash/argon2/blake2b-long.c',
              'libsodium/src/libsodium/crypto_pwhash/argon2/pwhash_argon2i.c',
              'libsodium/src/libsodium/crypto_pwhash/crypto_pwhash.c',
              'libsodium/src/libsodium/crypto_pwhash/scryptsalsa208sha256/crypto_scrypt-common.c',
              'libsodium/src/libsodium/crypto_pwhash/scryptsalsa208sha256/nosse/pwhash_scryptsalsa208sha256_nosse.c',
              'libsodium/src/libsodium/crypto_pwhash/scryptsalsa208sha256/pbkdf2-sha256.c',
              'libsodium/src/libsodium/crypto_pwhash/scryptsalsa208sha256/pwhash_scryptsalsa208sha256.c',
              'libsodium/src/libsodium/crypto_pwhash/scryptsalsa208sha256/scrypt_platform.c',
              'libsodium/src/libsodium/crypto_pwhash/scryptsalsa208sha256/sse/pwhash_scryptsalsa208sha256_sse.c',
              'libsodium/src/libsodium/crypto_scalarmult/crypto_scalarmult.c',
              'libsodium/src/libsodium/crypto_scalarmult/curve25519/donna_c64/curve25519_donna_c64.c',
              'libsodium/src/libsodium/crypto_scalarmult/curve25519/ref10/x25519_ref10.c',
              'libsodium/src/libsodium/crypto_scalarmult/curve25519/sandy2x/curve25519_sandy2x.c',
              'libsodium/src/libsodium/crypto_scalarmult/curve25519/sandy2x/fe51_invert.c',
              'libsodium/src/libsodium/crypto_scalarmult/curve25519/sandy2x/fe_frombytes_sandy2x.c',
              'libsodium/src/libsodium/crypto_scalarmult/curve25519/scalarmult_curve25519.c',
              'libsodium/src/libsodium/crypto_secretbox/crypto_secretbox.c',
              'libsodium/src/libsodium/crypto_secretbox/crypto_secretbox_easy.c',
              'libsodium/src/libsodium/crypto_secretbox/xsalsa20poly1305/ref/box_xsalsa20poly1305.c',
              'libsodium/src/libsodium/crypto_secretbox/xsalsa20poly1305/secretbox_xsalsa20poly1305_api.c',
              'libsodium/src/libsodium/crypto_shorthash/crypto_shorthash.c',
              'libsodium/src/libsodium/crypto_shorthash/siphash24/ref/shorthash_siphash24.c',
              'libsodium/src/libsodium/crypto_shorthash/siphash24/shorthash_siphash24_api.c',
              'libsodium/src/libsodium/crypto_sign/crypto_sign.c',
              'libsodium/src/libsodium/crypto_sign/ed25519/ref10/keypair.c',
              'libsodium/src/libsodium/crypto_sign/ed25519/ref10/obsolete.c',
              'libsodium/src/libsodium/crypto_sign/ed25519/ref10/open.c',
              'libsodium/src/libsodium/crypto_sign/ed25519/ref10/sign.c',
              'libsodium/src/libsodium/crypto_sign/ed25519/sign_ed25519_api.c',
              'libsodium/src/libsodium/crypto_stream/aes128ctr/portable/afternm_aes128ctr.c',
              'libsodium/src/libsodium/crypto_stream/aes128ctr/portable/beforenm_aes128ctr.c',
              'libsodium/src/libsodium/crypto_stream/aes128ctr/portable/consts_aes128ctr.c',
              'libsodium/src/libsodium/crypto_stream/aes128ctr/portable/int128_aes128ctr.c',
              'libsodium/src/libsodium/crypto_stream/aes128ctr/portable/stream_aes128ctr.c',
              'libsodium/src/libsodium/crypto_stream/aes128ctr/portable/xor_afternm_aes128ctr.c',
              'libsodium/src/libsodium/crypto_stream/aes128ctr/stream_aes128ctr_api.c',
              'libsodium/src/libsodium/crypto_stream/chacha20/ref/stream_chacha20_ref.c',
              'libsodium/src/libsodium/crypto_stream/chacha20/stream_chacha20.c',
              'libsodium/src/libsodium/crypto_stream/chacha20/vec/stream_chacha20_vec.c',
              'libsodium/src/libsodium/crypto_stream/crypto_stream.c',
              'libsodium/src/libsodium/crypto_stream/salsa20/ref/stream_salsa20_ref.c',
              'libsodium/src/libsodium/crypto_stream/salsa20/ref/xor_salsa20_ref.c',
              'libsodium/src/libsodium/crypto_stream/salsa20/stream_salsa20_api.c',
              'libsodium/src/libsodium/crypto_stream/salsa2012/ref/stream_salsa2012.c',
              'libsodium/src/libsodium/crypto_stream/salsa2012/ref/xor_salsa2012.c',
              'libsodium/src/libsodium/crypto_stream/salsa2012/stream_salsa2012_api.c',
              'libsodium/src/libsodium/crypto_stream/salsa208/ref/stream_salsa208.c',
              'libsodium/src/libsodium/crypto_stream/salsa208/ref/xor_salsa208.c',
              'libsodium/src/libsodium/crypto_stream/salsa208/stream_salsa208_api.c',
              'libsodium/src/libsodium/crypto_stream/xsalsa20/ref/stream_xsalsa20.c',
              'libsodium/src/libsodium/crypto_stream/xsalsa20/ref/xor_xsalsa20.c',
              'libsodium/src/libsodium/crypto_stream/xsalsa20/stream_xsalsa20_api.c',
              'libsodium/src/libsodium/crypto_verify/16/ref/verify_16.c',
              'libsodium/src/libsodium/crypto_verify/16/verify_16_api.c',
              'libsodium/src/libsodium/crypto_verify/32/ref/verify_32.c',
              'libsodium/src/libsodium/crypto_verify/32/verify_32_api.c',
              'libsodium/src/libsodium/crypto_verify/64/ref/verify_64.c',
              'libsodium/src/libsodium/crypto_verify/64/verify_64_api.c',
              'libsodium/src/libsodium/randombytes/nativeclient/randombytes_nativeclient.c',
              'libsodium/src/libsodium/randombytes/randombytes.c',
              'libsodium/src/libsodium/randombytes/salsa20/randombytes_salsa20_random.c',
              'libsodium/src/libsodium/randombytes/sysrandom/randombytes_sysrandom.c',
            ]
        }
    ]
}