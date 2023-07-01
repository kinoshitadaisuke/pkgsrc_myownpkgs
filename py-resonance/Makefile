# $NetBSD$

GITHUB_TAG=	refs/tags/v${PKGVERSION_NOREV}
DISTNAME=	resonance-0.22.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	math python
MASTER_SITES=	${MASTER_SITE_GITHUB:=moorepants/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/moorepants/resonance/
COMMENT=	Learning mechanical vibrations through computation
LICENSE=	mit

WRKSRC=		${WRKDIR}/${DISTNAME}

PYTHON_VERSIONS_INCOMPATIBLE=	27 37

DEPENDS+=	${PYPKGPREFIX}-matplotlib>=2.1:../../graphics/py-matplotlib
DEPENDS+=	${PYPKGPREFIX}-pandas>=0.17:../../math/py-pandas
DEPENDS+=	${PYPKGPREFIX}-scipy>=0.19:../../math/py-scipy
DEPENDS+=	${PYPKGPREFIX}-sympy>=1.1:../../math/py-sympy
DEPENDS+=	${PYPKGPREFIX}-notebook>=0:../../www/py-notebook
DEPENDS+=	${PYPKGPREFIX}-ipywidgets>=0:../../www/py-ipywidgets

BUILD_DEPENDS+=	${PYPKGPREFIX}-setuptools>=39.0:../../devel/py-setuptools
BUILD_DEPENDS+=	${PYPKGPREFIX}-pip>=9.0:../../devel/py-pip
BUILD_DEPENDS+=	${PYPKGPREFIX}-test>=0:../../devel/py-test
BUILD_DEPENDS+=	${PYPKGPREFIX}-test-cov>=0:../../devel/py-test-cov
BUILD_DEPENDS+=	${PYPKGPREFIX}-coverage>=0:../../devel/py-coverage
BUILD_DEPENDS+=	${PYPKGPREFIX}-sphinx>=0:../../textproc/py-sphinx
BUILD_DEPENDS+=	${PYPKGPREFIX}-jupyter-sphinx>=0.0:../../pkgsrc_myownpkgs/py-jupyter-sphinx

USE_LANGUAGES=	# none

BUILDLINK_API_DEPENDS.py-numpy+=	${PYPKGPREFIX}-numpy>=1.13
.include "../../math/py-numpy/buildlink3.mk"
.include "../../lang/python/egg.mk"
.include "../../mk/bsd.pkg.mk"
