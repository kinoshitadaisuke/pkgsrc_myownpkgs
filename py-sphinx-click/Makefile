# $NetBSD$

DISTNAME=	sphinx_click-6.2.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME:S/sphinx_click/sphinx-click/}
CATEGORIES=	textproc python
MASTER_SITES=	${MASTER_SITE_PYPI:=s/sphinx-click/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/sphinx-click/
COMMENT=	TODO: Short description of the package
#LICENSE=	# TODO: (see mk/license.mk)

BUILD_DEPENDS+=	${PYPKGPREFIX}-pbr>=2.0:../../devel/py-pbr
BUILD_DEPENDS+=	${PYPKGPREFIX}-setuptools>=0:../../devel/py-setuptools
DEPENDS+=	${PYPKGPREFIX}-mypy>=0:../../lang/py-mypy
DEPENDS+=	${PYPKGPREFIX}-flake8>=0:../../devel/py-flake8

USE_LANGUAGES=	# none

#.include "../../lang/python/egg.mk"
.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
