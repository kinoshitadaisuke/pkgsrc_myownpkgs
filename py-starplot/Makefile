# $NetBSD$

GITHUB_PROJECT=	starplot
DISTNAME=	0.19.0
GITHUB_TAG=	refs/tags/v${DISTNAME}
PKGNAME=	${PYPKGPREFIX}-${GITHUB_PROJECT}-${DISTNAME}
CATEGORIES=	math python
MASTER_SITES=	${MASTER_SITE_GITHUB:=steveberardi/}
DIST_SUBDIR=	${GITHUB_PROJECT}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/steveberardi/starplot/
COMMENT=	Python library for creating star charts and maps
LICENSE=	mit

WRKSRC=	${WRKDIR}/${GITHUB_PROJECT}-${DISTNAME}

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

post-install:
	cd ${DESTDIR}${PREFIX}/bin && \
	${MV} starplot starplot-${PYVERSSUFFIX} || ${TRUE}

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
