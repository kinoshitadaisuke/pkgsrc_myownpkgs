# $NetBSD$

DISTNAME=	geopy-2.4.1
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	geography python
MASTER_SITES=	${MASTER_SITE_PYPI:=g/geopy/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/geopy/
COMMENT=	Geocoding library for Python
LICENSE=	mit

TOOL_DEPENDS+=	${PYPKGPREFIX}-coverage>=0:../../devel/py-coverage
TOOL_DEPENDS+=	${PYPKGPREFIX}-flake8>=5.0:../../devel/py-flake8
TOOL_DEPENDS+=	${PYPKGPREFIX}-isort>=5.10.0:../../devel/py-isort
TOOL_DEPENDS+=	${PYPKGPREFIX}-readme_renderer>=0:../../textproc/py-readme_renderer
TOOL_DEPENDS+=	${PYPKGPREFIX}-sphinx-issues>=0:../../textproc/py-sphinx-issues
TOOL_DEPENDS+=	${PYPKGPREFIX}-sphinx-rtd-theme>=0.5.0:../../textproc/py-sphinx-rtd-theme
TOOL_DEPENDS+=	${PYPKGPREFIX}-test>=3.10:../../devel/py-test
TOOL_DEPENDS+=	${PYPKGPREFIX}-test-asyncio>=0.17:../../devel/py-test-asyncio
TOOL_DEPENDS+=	${PYPKGPREFIX}-sphinx>=0:../../textproc/py-sphinx

DEPENDS+=	${PYPKGPREFIX}-geographiclib>=0:../../pkgsrc_myownpkgs/py-geographiclib

USE_LANGUAGES=	# none

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
