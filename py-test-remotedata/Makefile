# $NetBSD$

DISTNAME=	pytest_remotedata-0.4.2
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=p/pytest_remotedata/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/pytest_remotedata/
COMMENT=	Plugin to control whether tests are run that have remote data
LICENSE=	bsd-modified

USE_LANGUAGES=	# none

BUILD_DEPENDS+=	${PYPKGPREFIX}-setuptools>=77.0.1:../../devel/py-setuptools
BUILD_DEPENDS+=	${PYPKGPREFIX}-setuptools_scm>=0:../../devel/py-setuptools_scm

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
