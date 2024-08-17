# $NetBSD$

DISTNAME=	# empty
PKGNAME=	meta-www-1.0
PKGREVISION=	0
CATEGORIES=	meta-pkgs net www
MASTER_SITES=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
DISTFILES=	# empty

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
COMMENT=	Meta package for web server
LICENSE=	modified-bsd

META_PACKAGE=	yes

.include "../../mk/bsd.prefs.mk"

# security
DEPENDS+=	${PYPKGPREFIX}-certbot>=0:../../security/py-certbot
DEPENDS+=	openssl>=0:../../security/openssl

# www
DEPENDS+=	apache>=0:../../www/apache24

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
