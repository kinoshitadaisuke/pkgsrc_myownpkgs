# $NetBSD: buildlink3.mk,v 1.63 2024/11/01 12:54:49 wiz Exp $

BUILDLINK_TREE+=	curl

.if !defined(CURL_BUILDLINK3_MK)
CURL_BUILDLINK3_MK:=

BUILDLINK_API_DEPENDS.curl+=	curl>=7.12.3
BUILDLINK_ABI_DEPENDS.curl+=	curl>=8.10.1nb2
BUILDLINK_PKGSRCDIR.curl?=	../../pkgsrc_myownpkgs/curl

pkgbase:= curl
.include "../../mk/pkg-build-options.mk"
.if ${PKG_BUILD_OPTIONS.curl:Mlibssh2}
.  include "../../security/libssh2/buildlink3.mk"
.endif
.if ${PKG_BUILD_OPTIONS.curl:Mgssapi}
.  include "../../mk/krb5.buildlink3.mk"
.endif
.if ${PKG_BUILD_OPTIONS.curl:Mldap}
.  include "../../databases/openldap-client/buildlink3.mk"
.endif
.if ${PKG_BUILD_OPTIONS.curl:Mrtmp}
.  include "../../net/rtmpdump/buildlink3.mk"
.endif
.if ${PKG_BUILD_OPTIONS.curl:Midn}
.  include "../../devel/libidn2/buildlink3.mk"
.endif
.if ${PKG_BUILD_OPTIONS.curl:Mhttp2}
.  include "../../www/nghttp2/buildlink3.mk"
.endif
.if ${PKG_BUILD_OPTIONS.curl:Mbrotli}
.  include "../../archivers/brotli/buildlink3.mk"
.endif
.if ${PKG_BUILD_OPTIONS.curl:Mzstd}
.  include "../../archivers/zstd/buildlink3.mk"
.endif

.include "../../devel/gettext-lib/buildlink3.mk"
.include "../../devel/zlib/buildlink3.mk"
.include "../../security/openssl/buildlink3.mk"
.endif # CURL_BUILDLINK3_MK

BUILDLINK_TREE+=	-curl
