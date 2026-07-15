# $NetBSD$

DISTNAME=	pathvalidate-3.3.1
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=p/pathvalidate/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/thombashi/pathvalidate
COMMENT=	library to sanitize/validate a string such as filenames/paths
LICENSE=	mit

USE_LANGUAGES=	# none

BUILD_DEPENDS+=	${PYPKGPREFIX}-setuptools>=64:../../devel/py-setuptools
BUILD_DEPENDS+=	${PYPKGPREFIX}-setuptools_scm>=8:../../devel/py-setuptools_scm

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
