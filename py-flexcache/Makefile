# $NetBSD$

DISTNAME=       flexcache-0.3
PKGNAME=        ${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=     devel python
MASTER_SITES=   ${MASTER_SITE_PYPI:=f/flexcache/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/hgrecco/flexcache/
COMMENT=	cache the result of expensive calculations on the disk
LICENSE=	modified-bsd

USE_LANGUAGES=	# none

PYTHON_VERSIONS_INCOMPATIBLE=	27

BUILD_DEPENDS+= ${PYPKGPREFIX}-setuptools>=61:../../devel/py-setuptools
BUILD_DEPENDS+= ${PYPKGPREFIX}-setuptools_scm>=3.4.3:../../devel/py-setuptools_scm

DEPENDS+=       ${PYPKGPREFIX}-typing-extensions>=0:../../devel/py-typing-extensions

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
