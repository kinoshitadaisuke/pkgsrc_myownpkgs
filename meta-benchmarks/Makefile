# $NetBSD$

DISTNAME=	# empty
PKGNAME=	meta-benchmarks-1.0
PKGREVISION=	0
CATEGORIES=	meta-pkgs benchmarks
MASTER_SITES=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
DISTFILES=	# empty

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
COMMENT=	Meta package for benchmarks
LICENSE=	modified-bsd

META_PACKAGE=	yes

.include "../../mk/bsd.prefs.mk"

# security
DEPENDS+=	mozilla-rootcerts-openssl>=0:../../security/mozilla-rootcerts-openssl

# benchmarks
DEPENDS+=	dhrystone>=0:../../benchmarks/dhrystone
DEPENDS+=	fib>=0:../../benchmarks/fib
DEPENDS+=	flops>=0:../../benchmarks/flops
DEPENDS+=	heapsort>=0:../../benchmarks/heapsort
DEPENDS+=	nsieve>=0:../../benchmarks/nsieve
DEPENDS+=	ubench>=0:../../benchmarks/ubench
DEPENDS+=	whetstone>=0:../../benchmarks/whetstone
DEPENDS+=	xengine>=0:../../benchmarks/xengine

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
