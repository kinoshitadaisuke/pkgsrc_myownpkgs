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

# lang
DEPENDS+=	php83>=0:../../lang/php83
#DEPENDS+=	php84>=0:../../lang/php84

# security
DEPENDS+=	${PYPKGPREFIX}-certbot>=0:../../security/py-certbot
DEPENDS+=	openssl>=0:../../security/openssl

# www
DEPENDS+=	apache>=0:../../www/apache24
DEPENDS+=	ap-php>=0:../../www/ap-php

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
