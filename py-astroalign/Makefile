# $NetBSD$

GITHUB_PROJECT=	astroalign
GITHUB_TAG=	refs/tags/v${PKGVERSION_NOREV}
DISTNAME=	astroalign-2.5.1
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	math python
MASTER_SITES=	${MASTER_SITE_GITHUB:=quatrope/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/astroalign/
COMMENT=	Python module for aligning astronomical images
LICENSE=	mit

WRKSRC=	${WRKDIR}/${DISTNAME}

USE_LANGUAGES=	# none

PYTHON_VERSIONS_INCOMPATIBLE=	27

DEPENDS+=	${PYPKGPREFIX}-setuptools>=0:../../devel/py-setuptools
DEPENDS+=	${PYPKGPREFIX}-numpy>=1.11:../../math/py-numpy
DEPENDS+=	${PYPKGPREFIX}-scipy>=0.15:../../math/py-scipy
DEPENDS+=	${PYPKGPREFIX}-scikit-image>=0:../../math/py-scikit-image
DEPENDS+=	${PYPKGPREFIX}-sep>=0:../../pkgsrc_myownpkgs/py-sep

.include "../../lang/python/egg.mk"
.include "../../mk/bsd.pkg.mk"
