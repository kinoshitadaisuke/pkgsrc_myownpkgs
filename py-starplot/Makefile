# $NetBSD$

GITHUB_TAG=	refs/tags/v${PKGVERSION_NOREV}
DISTNAME=	starplot-0.1.2
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	math python
MASTER_SITES=	${MASTER_SITE_GITHUB:=steveberardi/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/steveberardi/starplot/
COMMENT=	Python library for creating star charts and maps
LICENSE=	mit

WRKSRC=	${WRKDIR}/${DISTNAME}

USE_LANGUAGES=	# none

PYTHON_VERSIONS_INCOMPATIBLE=	27

DEPENDS+=	${PYPKGPREFIX}-flit_core>=3.2:../../devel/py-flit_core
DEPENDS+=	${PYPKGPREFIX}-matplotlib>=3.5.1:../../graphics/py-matplotlib
DEPENDS+=	${PYPKGPREFIX}-numpy>=1.22.1:../../math/py-numpy
DEPENDS+=	${PYPKGPREFIX}-pandas>=1.4.0:../../math/py-pandas
DEPENDS+=	${PYPKGPREFIX}-pydantic>=1.10.8:../../devel/py-pydantic
DEPENDS+=	${PYPKGPREFIX}-skyfield>=1.41:../../pkgsrc_myownpkgs/py-skyfield
DEPENDS+=	${PYPKGPREFIX}-adjusttext>=0.8:../../pkgsrc_myownpkgs/py-adjusttext
DEPENDS+=	${PYPKGPREFIX}-sgp4>=0:../../pkgsrc_myownpkgs/py-sgp4

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
