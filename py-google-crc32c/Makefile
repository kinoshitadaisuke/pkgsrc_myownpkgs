# $NetBSD$

DISTNAME=	google_crc32c-1.8.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME:S/_/-/}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=g/google_crc32c/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/google_crc32c/
COMMENT=	Python wrapper of the C library Google CRC32C
LICENSE=	apache-2.0

DEPENDS+=	${PYPKGPREFIX}-setuptools>=0:../../devel/py-setuptools

# url2pkg-marker (please do not remove this line.)
.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
